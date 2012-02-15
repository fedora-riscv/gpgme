/* This file is here to prevent a file conflict on multiarch systems.
 * A conflict will frequently occur because arch-specific build-time
 * configuration options are stored in gpgme.h. By stripping them we would
 * risk for issues like bug 621698 to stay unnoticed. This file is inspired
 * by opensslconf-new.h.
 * DO NOT INCLUDE THE NEW FILE DIRECTLY -- ALWAYS INCLUDE THIS ONE INSTEAD. */

#ifdef gpgme_gpgme_multilib_redirection_h
#error "Do not define gpgme_gpgme_multilib_redirection_h!"
#endif
#define gpgme_gpgme_multilib_redirection_h

#if defined(__i386__)
#include "gpgme-i386.h"
#elif defined(__ia64__)
#include "gpgpme-ia64.h"
#elif defined(__powerpc64__)
#include "gpgme-ppc64.h"
#elif defined(__powerpc__)
#include "gpgme-ppc.h"
#elif defined(__s390x__)
#include "gpgme-s390x.h"
#elif defined(__s390__)
#include "gpgme-s390.h"
#elif defined(__sparc__) && defined(__arch64__)
#include "gpgme-sparc64.h"
#elif defined(__sparc__)
#include "gpgme-sparc.h"
#elif defined(__x86_64__)
#include "gpgme-x86_64.h"
#else
#error "This gpgme-devel package does not work your architecture?"
#endif

#undef gpgme_gpgme_multilib_redirection_h

